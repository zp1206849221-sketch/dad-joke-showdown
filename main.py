import os

JOKE = "I told my suitcase there would be no vacation this year. Now I'm dealing with emotional baggage."

def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(JOKE)
    os.chmod("/output/entry.txt", 0o644)

if __name__ == "__main__":
    main()
