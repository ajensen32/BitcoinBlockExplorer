using BitcoinExplorer.Models;
using System.Net.Http.Json; // Add this using directive to include the System.Net.Http.Json namespace
using System.Threading.Tasks; // Add this using directive to include the System.Threading.Tasks namespace   

namespace BlockExplorer.Services
{
    public class BlockService
    {
        private readonly HttpClient _http;

        public BlockService(HttpClient http)
        {
            _http = http;
        }

        public async Task<BlockData> GetBlockAsync(int height)
        {
            BlockData? blockData = await _http.GetFromJsonAsync<BlockData>($"http://localhost:5000/block/{height}");
            if (blockData == null)
            {
                throw new InvalidOperationException("Block data was null.");
            }

            return blockData;
        }

        public async Task<TransactionData> GetTransactioNAsync(string txid)
        {
            TransactionData? txData = await _http.GetFromJsonAsync<TransactionData>($"http://localhost:5000/tx/{txid}");
            if (txData == null)
            {
                throw new InvalidOperationException("Transaction data was null.");
            }
            return txData;
        }

    }

}
