import requests  # type: ignore
import json  # type: ignore
from flask import Flask, Response, jsonify  # type: ignore
from flask_cors import CORS  # type: ignore

app = Flask(__name__)
CORS(app)

# ---- GET BLOCK BY HEIGHT ----
@app.route('/block/<int:height>')
def get_block(height):
    try:
        # 1. Get block hash from height
        hash_response = requests.get(f'https://blockstream.info/api/block-height/{height}')
        if hash_response.status_code != 200:
            return jsonify({"error": "Block not found"}), 404
        block_hash = hash_response.text

        # 2. Get block metadata
        block_response = requests.get(f'https://blockstream.info/api/block/{block_hash}')
        block_data = block_response.json()

        # 3. Get transactions in block (first page only)
        tx_response = requests.get(f'https://blockstream.info/api/block/{block_hash}/txs')
        tx_list = tx_response.json()
        txids = [tx.get("txid") for tx in tx_list]

        result = {
            "height": height,
            "hash": block_data.get("id"),
            "time": block_data.get("timestamp"),
            "transactions": txids
        }

        return Response(json.dumps(result), mimetype="application/json")

    except Exception as e:
        return jsonify({"error": str(e)}), 500


# ---- GET TRANSACTION BY TXID ----
@app.route('/tx/<txid>')
def get_transaction(txid):
    try:
        tx_response = requests.get(f'https://blockstream.info/api/tx/{txid}')
        if tx_response.status_code != 200:
            return jsonify({"error": "Transaction not found"}), 404
        tx_data = tx_response.json()

        # Inputs
        inputs = []
        for vin in tx_data.get("vin", []):
            vout_value = vin.get("vout")
            inputs.append({
                "prev_tx": vin.get("txid", "coinbase"),
                "index": vout_value if isinstance(vout_value, int) else None
            })

        # Outputs
        outputs = []
        for vout in tx_data.get("vout", []):
            addr = vout.get("scriptpubkey_address", "unknown")
            value = vout.get("value", 0) / 1e8  # satoshis to BTC
            outputs.append({
                "address": addr,
                "value": value
            })

        result = {
            "txid": tx_data.get("txid"),
            "inputs": inputs,
            "outputs": outputs
        }

        print("=== JSON SENT TO FRONTEND ===")
        print(json.dumps(result, indent=2))

        return Response(json.dumps(result), mimetype="application/json")

    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__ == '__main__':
    app.run(port=5000)
