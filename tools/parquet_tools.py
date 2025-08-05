from server import mcp
from utils.file_reader import read_parquet_summary


@mcp.tool()
def summarize_parquet_file(filename: str) -> str:
    return read_parquet_summary(filename)
