import sys


def main():
    name = sys.argv[1] if len(sys.argv) > 1 else "世界"
    print(f"你好，{name}！这是从 GitHub 克隆下来的代码。")


if __name__ == "__main__":
    main()
