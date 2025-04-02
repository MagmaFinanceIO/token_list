import json
from pathlib import Path

def merge_coin_files(input_dir="../coin_info", output_file="merged_coins.json"):
    merged_data = []
    processed_coins = set()
    input_path = Path(input_dir)

    if not input_path.exists():
        print(f"Error：input dir {input_dir} not exist")
        return

    for file_path in input_path.glob("*.json"):
        try:
            with open(file_path, "r", encoding="utf-8") as f:
                entry = json.load(f)

                coin_type = entry.get("coin_type")
                if not coin_type:
                    print(f"Warning: {file_path.name} coin_type not exist，skipping")
                    continue

                if coin_type in processed_coins:
                    print(f"Warning：duplicate coin_type: {coin_type}，skipping")
                    continue

                merged_data.append(entry)
                processed_coins.add(coin_type)

        except json.JSONDecodeError:
            print(f"Error：file {file_path.name} invalid JSON content")
        except Exception as e:
            print(f"Error: reading {file_path.name}：{str(e)}")

    try:
        with open(output_file, "w", encoding="utf-8") as f:
            json.dump(merged_data, f, ensure_ascii=False, indent=2)
        print(f"\nMerge {len(merged_data)} items into {output_file}")
    except Exception as e:
        print(f"Failed to write merged file：{str(e)}")

if __name__ == "__main__":
    merge_coin_files()
