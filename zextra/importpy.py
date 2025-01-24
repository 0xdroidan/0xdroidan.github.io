import os

# Directory path to check the files
directory_path = "/home/shivam/Work/0xdroidan.github.io/_posts"

data = [
    ("Avalanche Retrodrop (Retro9000)", "2024-12-19", "Layer 1"),
    ("Pudgy Penguins", "2024-12-17", "NFT"),
    ("Anzen", "2024-12-13", "RWA"),
    ("WalletConnect", "2024-11-27", "Wallet"),
    ("Movement", "2024-11-26", "Layer 1"),
    ("DeepBook", "2024-11-14", "DEX"),
    ("Optimism", "2024-10-10", "Network"),
    ("Phaver", "2024-09-26", "SocialFi"),
    ("LayerZero", "2024-09-21", "Bridge"),
    ("ZetaChain Season 1", "2024-09-19", "Layer 2"),
    ("MON Protocol", "2024-09-07", "GameFi"),
    ("EigenLayer Season 2", "2024-09-05", "Restaking"),
    ("Grass", "2024-09-05", "DePIN"),
    ("Sharpe", "2024-09-01", "Perps"),
    ("GammaSwap", "2024-08-28", "Perps"),
    ("Layer3", "2024-08-10", "Quest"),
    ("Aigisos", "2024-08-06", "AI"),
    ("deBridge #1", "2024-07-24", "Bridge"),
    ("EtherFi Season 2", "2024-07-18", "Restaking"),
    ("Sanctum", "2024-07-18", "LST"),
    ("Lava", "2024-07-10", "Infrastructure"),
    ("Zircuit", "2024-07-07", "Layer 2"),
    ("Penumbra", "2024-07-06", "Infrastructure"),
    ("Zeta Markets", "2024-06-27", "Perps"),
    ("Blast", "2024-06-26", "Layer 2"),
    ("Orderly", "2024-06-24", "Perps"),
    ("LayerZero", "2024-06-20", "Bridge"),
    ("Mocaverse", "2024-06-19", "SocialFi"),
    ("Nyan Heroes", "2024-06-14", "GameFi"),
    ("ListaDAO", "2024-06-14", "Stablecoin"),
    ("Azuro", "2024-06-13", "GambleFi"),
    ("Nostra", "2024-06-13", "Lending"),
    ("zkSync", "2024-06-11", "Layer 2"),
    ("zkLink", "2024-06-01", "Layer 2"),
    ("Uprock", "2024-05-28", "DePIN"),
    ("Sei", "2024-05-28", "Layer 1"),
    ("Taiko #1", "2024-05-23", "Layer 2"),
    ("Avalanche Community Drop", "2024-05-20", "Layer 1"),
    ("Notcoin", "2024-05-16", "GameFi"),
    ("BounceBit", "2024-05-13", "BTCFi"),
    ("EigenLayer Season 1", "2024-05-10", "Restaking"),
    ("Polyhedra", "2024-05-06", "Bridge"),
    ("ionet", "2024-05-06", "AI"),
    ("Spectral Labs #1", "2024-05-06", "AI"),
    ("Mode", "2024-05-03", "Layer 2"),
    ("Drift", "2024-05-01", "DEX"),
    ("Renzo", "2024-04-26", "Restaking"),
    ("Aethir", "2024-04-25", "AI"),
    ("Avail", "2024-04-18", "Infrastructure"),
    ("Soarchain Genesis Drop", "2024-04-15", "DePIN"),
    ("Parcl", "2024-04-15", "RWA"),
    ("Omni", "2024-04-11", "Infrastructure"),
    ("Wen", "2024-04-11", "Meme Coin"),
    ("Tensor", "2024-04-08", "NFT Marketplace"),
    ("Zeus", "2024-04-05", ""),
    ("Kamino", "2024-03-31", "Lending"),
    ("Ethena", "2024-03-28", "DeFi"),
    ("EtherFi", "2024-03-18", "Restaking"),
    ("Aevo", "2024-03-13", "Perps"),
    ("Wormhole", "2024-03-07", "Bridge"),
    ("Fluidity", "2024-03-06", "DeFi"),
    ("Bonsai", "2024-03-05", "SocialFi"),
    ("Portal", "2024-03-01", "GameFi"),
    ("QnA3", "2024-02-28", "SocialFi"),
    ("Optimism #4", "2024-02-21", "Network"),
    ("Pixels (RON Staking)", "2024-02-18", "GameFi"),
    ("De.Fi", "2024-02-15", "DeFi"),
    ("Starknet", "2024-02-14", "Network"),
    ("Dmail #1", "2024-01-30", "DeFi"),
    ("SailDAO", "2024-01-30", "DeFi"),
    ("ZetaChain", "2024-01-25", "Network"),
    ("AltLayer", "2024-01-23", "Infrastructure"),
    ("Magic Square", "2024-01-10", "SocialFi"),
    ("Degen", "2024-01-09", "SocialFi"),
    ("XAI", "2024-01-09", "GameFi"),
    ("Mavia", "2024-01-05", "GameFi"),
    ("Manta", "2024-01-05", "Layer 2"),
    ("Port3", "2024-01-05", "GameFi,SocialFi"),
    ("Saga", "2024-01-05", ""),
    ("Dymension", "2024-01-02", ""),
    ("zkFair", "2024-01-01", "Layer 2"),
    ("NFPrompt", "2023-12-27", "DeFi"),
    ("Nois Randdrop (Osmo)", "2023-12-19", "Network"),
    ("AsMatch", "2023-12-15", "SocialFi"),
    ("Seamless", "2023-12-11", "DeFi"),
    ("Namada", "2023-12-07", ""),
    ("Jito", "2023-12-05", "LST"),
    ("Quasar", "2023-12-01", "DeFi"),
    ("Holdstation #1", "2023-11-25", "Wallet"),
    ("Prisma Finance", "2023-11-04", "LST"),
    ("Memeland (Memecoin)", "2023-11-03", "Meme Coin"),
    ("Jupiter", "2023-11-02", "DEX"),
    ("Pyth Network", "2023-11-01", "Infrastructure"),
    ("Celestia", "2023-10-19", "Network"),
    ("ZTX", "2023-10-16", "GameFi"),
    ("Raft", "2023-10-11", "Lending"),
    ("Islamic Coin", "2023-10-11", "Network"),
    ("Optimism #3", "2023-09-18", "Network"),
    ("zkSwap", "2023-08-22", "DEX"),
    ("Connext", "2023-08-18", "Bridge"),
    ("Altitude (LayerZero)", "2023-08-16", "Bridge"),
    ("Sei #1", "2023-08-15", "Network"),
    ("Clipper", "2023-08-09", "DEX"),
    ("Orchai", "2023-08-07", ""),
    ("Aerodrome", "2023-08-05", "DEX"),
    ("CyberConnect", "2023-08-04", "SocialFi"),
    ("SpartaDEX", "2023-07-21", "DEX,GameFi"),
    ("GameSwift", "2023-07-15", "GameFi"),
    ("Archway", "2023-07-06", "Network"),
    ("Space ID #2", "2023-06-29", "Domain"),
    ("Maverick", "2023-06-28", "DEX"),
    ("Pika", "2023-06-19", "DEX"),
    ("Virtuswap", "2023-05-22", "DEX"),
    ("zkApe", "2023-05-07", "DeFi"),
    ("Antimatter", "2023-04-20", "Network"),
    ("Arbitrum", "2023-03-23", "Network"),
    ("Space_ID", "2023-03-19", "Domain"),
    ("Vita", "2023-02-26", "Gaming"),
]


# Function to check if the file is empty and write details based on file name
def check_and_write_file(directory_path, data):
    try:
        # Loop through each file in the directory
        for filename in os.listdir(directory_path):
            file_path = os.path.join(directory_path, filename)

            # Skip directories
            if os.path.isdir(file_path):
                continue

            # Check if the file name matches any title in the data
            for title, date, categories in data:
                if filename.lower().startswith(title.lower()):  # Match the file name to the title (case insensitive)
                    # Open the file and check if it is empty
                    with open(file_path, "r") as file:
                        content = file.read()
                        if content.strip():  # If the file is not empty
                            print(f"File {filename} already contains content.")
                            continue  # Skip this file and move to the next

                    # If the file is empty, write the data including categories
                    with open(file_path, "a") as file:
                        file.write(f"""---
layout: post
title: "{title}"
date: {date}
categories: [{categories}]
tags: [all]

---

## [Project Website](link)

Short Project Description

## Token claim

Eligible User : not known  
Number of Claimants : not known

## Project Ticker

## Airdrop Type

## Airdrop Timeline

| Blockchain snapshot     | Claiming Started           | Claiming ends    |
| ----------------------- |:--------------------------:| ----------------:|
|       not known         |        not known           |   not known      |

## Amount Received in tokens  

| Max        |    Median / Average  |       Min    |
| ---------- |:--------------------:| ------------:|
| not known  |     not known        |  not known   |

For checking price visit [coinmarketcap](https://coinmarketcap.com/currencies/) and [coingecko](https://www.coingecko.com/en/coins/)

## [Criteria For Airdrop](link)

## Any other links
                        """)

                        print(f"Data has been written to {filename}.")
                    break  # Move to the next file after updating one

    except Exception as e:
        print(f"Error occurred: {e}")

# Call the function to process the directory
check_and_write_file(directory_path, data)
