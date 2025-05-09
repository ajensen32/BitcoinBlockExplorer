<h1>Bitcoin Block Explorer 🔎</h1>

<p>
  A lightweight full-stack Bitcoin block explorer built with <strong>Python Flask</strong> and <strong>.NET Blazor Server</strong>. 
  This project allows users to search for Bitcoin block data by height and view detailed transaction information by transaction ID — all using live data from the Blockstream public REST API.
</p>

<hr />

<h2>📌 Features</h2>
<ul>
  <li>🔢 Search by block height — shows block hash, timestamp, and a list of transaction IDs</li>
  <li>🧾 Search by transaction ID — displays transaction inputs and outputs</li>
  <li>🔄 Clickable transaction IDs to load details instantly</li>
  <li>🧠 Handles coinbase transactions and large input indexes safely</li>
  <li>⚙️ Real-time data fetched from the Bitcoin blockchain via public APIs</li>
</ul>

<hr />

<h2>🛠️ Tech Stack</h2>
<ul>
  <li><strong>Frontend:</strong> Blazor Server (.NET 8), Razor Pages, HttpClient</li>
  <li><strong>Backend:</strong> Python Flask, Flask-CORS, Blockstream REST API</li>
  <li><strong>Communication:</strong> JSON over HTTP (localhost)</li>
</ul>

<hr />

<h2>🚀 How to Run Locally</h2>

<h3>1. Clone the repository</h3>
<pre><code>git clone https://github.com/your-username/bitcoin-block-explorer.git</code></pre>

<h3>2. Start the Python Flask backend</h3>
<pre><code>
cd backend
python -m venv venv
venv\Scripts\activate  # or source venv/bin/activate on Mac/Linux
pip install -r requirements.txt
python app.py
</code></pre>

<h3>3. Start the Blazor frontend</h3>
<pre><code>
cd frontend
dotnet run
</code></pre>

<h3>4. Open your browser</h3>
<ul>
  <li>Backend running at: <code>http://localhost:5000</code></li>
  <li>Frontend running at: <code>https://localhost:7227</code> (or your console output URL)</li>
</ul>

<hr />

<h2>🎯 Use Cases</h2>
<ul>
  <li>Educational tool for understanding how blockchain data is structured</li>
  <li>Demonstration of full-stack integration between Python and .NET</li>
  <li>Foundation for a production-ready block explorer or blockchain analytics tool</li>
</ul>

<hr />

<h2>📈 Future Improvements</h2>
<ul>
  <li>Add pagination for blocks with many transactions</li>
  <li>Improve UI/UX with Bootstrap or Tailwind CSS</li>
  <li>Deploy Flask backend to Render or Railway, and Blazor app to Azure</li>
  <li>Add charts, filters, and block navigation</li>
</ul>

<hr />

<h2>✅ Completed Functionality</h2>
<ul>
  <li>✔️ Fully functional block and transaction lookup</li>
  <li>✔️ Integrated frontend and backend</li>
  <li>✔️ Error handling and null value safety</li>
  <li>✔️ Deployment-ready architecture</li>
</ul>

<hr />

