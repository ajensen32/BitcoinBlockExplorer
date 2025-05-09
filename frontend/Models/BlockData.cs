
namespace BitcoinExplorer.Models
{
    public class BlockData
    {
        public int Height { get; set; }
        public string? Hash { get; set; }

        // ✅ Fix: use long? for Unix timestamp
        public long? Time { get; set; }

        public List<string>? Transactions { get; set; }
    }

    public class TransactionData
    {
        public string? Txid { get; set; }
        public List<Input>? Inputs { get; set; }
        public List<Output>? Outputs { get; set; }
    }

    public class Input
    {
        public string? PrevTx { get; set; }

        // Fix: index can be larger than Int32.MaxValue
        public long? Index { get; set; }
    }

    public class Output
    {
        public string? Address { get; set; }
        public double Value { get; set; }
    }

}

