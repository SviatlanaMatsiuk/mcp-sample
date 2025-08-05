from server import mcp
from utils.file_reader import read_csv_summary


@mcp.tool()
def summarize_csv_file(filename: str) -> str:
    return read_csv_summary(filename)
