import os

# List of titles and dates
data = [
    ("Avalanche Retrodrop (Retro9000)", "2024-12-19"),
    ("Pudgy Penguins", "2024-12-17"),
    ("Anzen", "2024-12-13"),
    ("WalletConnect", "2024-11-27"),
    ("Movement", "2024-11-26"),
    ("DeepBook", "2024-11-14"),
    ("Optimism", "2024-10-10"),
    ("Phaver", "2024-09-26"),
    ("LayerZero", "2024-09-21"),
    ("ZetaChain Season 1", "2024-09-19"),
    ("MON Protocol", "2024-09-07"),
    ("EigenLayer Season 2", "2024-09-05"),
    ("Grass", "2024-09-05"),
    ("Sharpe", "2024-09-01"),
    ("GammaSwap", "2024-08-28"),
    ("Layer3", "2024-08-10"),
    ("Aigisos", "2024-08-06"),
    ("deBridge #1", "2024-07-24"),
    ("EtherFi Season 2", "2024-07-18"),
    ("Sanctum", "2024-07-18"),
    ("Lava", "2024-07-10"),
    ("Zircuit", "2024-07-07"),
    ("Penumbra", "2024-07-06"),
    ("Zeta Markets", "2024-06-27"),
    ("Blast", "2024-06-26"),
    ("Orderly", "2024-06-24"),
    ("LayerZero", "2024-06-20"),
    ("Mocaverse", "2024-06-19"),
    ("Nyan Heroes", "2024-06-14"),
    ("ListaDAO", "2024-06-14"),
    ("Azuro", "2024-06-13"),
    ("Nostra", "2024-06-13"),
    ("zkSync", "2024-06-11"),
    ("zkLink", "2024-06-01"),
    ("Uprock", "2024-05-28"),
    ("Sei", "2024-05-28"),
    ("Taiko #1", "2024-05-23"),
    ("Avalanche Community Drop", "2024-05-20"),
    ("Notcoin", "2024-05-16"),
    ("BounceBit", "2024-05-13"),
    ("EigenLayer Season 1", "2024-05-10"),
    ("Polyhedra", "2024-05-06"),
    ("ionet", "2024-05-06"),
    ("Spectral Labs #1", "2024-05-06"),
    ("Mode", "2024-05-03"),
    ("Drift", "2024-05-01"),
    ("Renzo", "2024-04-26"),
    ("Aethir", "2024-04-25"),
    ("Avail", "2024-04-18"),
    ("Soarchain Genesis Drop", "2024-04-15"),
    ("Parcl", "2024-04-15"),
    ("Omni", "2024-04-11"),
    ("Wen", "2024-04-11"),
    ("Tensor", "2024-04-08"),
    ("Zeus", "2024-04-05"),
    ("Kamino", "2024-03-31"),
    ("Ethena", "2024-03-28"),
    ("EtherFi", "2024-03-18"),
    ("Aevo", "2024-03-13"),
    ("Wormhole", "2024-03-07"),
    ("Fluidity", "2024-03-06"),
    ("Bonsai", "2024-03-05"),
    ("Portal", "2024-03-01"),
    ("QnA3", "2024-02-28"),
    ("Optimism #4", "2024-02-21"),
    ("Pixels (RON Staking)", "2024-02-18"),
    ("De.Fi", "2024-02-15"),
    ("Starknet", "2024-02-14"),
    ("Dmail #1", "2024-01-30"),
    ("SailDAO", "2024-01-30"),
    ("ZetaChain", "2024-01-25"),
    ("AltLayer", "2024-01-23"),
    ("Magic Square", "2024-01-10"),
    ("Degen", "2024-01-09"),
    ("XAI", "2024-01-09"),
    ("Mavia", "2024-01-05"),
    ("Manta", "2024-01-05"),
    ("Port3", "2024-01-05"),
    ("Saga", "2024-01-05"),
    ("Dymension", "2024-01-02"),
    ("zkFair", "2024-01-01"),
    ("NFPrompt", "2023-12-27"),
    ("Nois Randdrop (Osmo)", "2023-12-19"),
    ("AsMatch", "2023-12-15"),
    ("Seamless", "2023-12-11"),
    ("Namada", "2023-12-07"),
    ("Jito", "2023-12-05"),
    ("Quasar", "2023-12-01"),
    ("Holdstation #1", "2023-11-25"),
    ("Prisma Finance", "2023-11-04"),
    ("Memeland (Memecoin)", "2023-11-03"),
    ("Jupiter", "2023-11-02"),
    ("Pyth Network", "2023-11-01"),
    ("Celestia", "2023-10-19"),
    ("ZTX", "2023-10-16"),
    ("Raft", "2023-10-11"),
    ("Islamic Coin", "2023-10-11"),
    ("Optimism #3", "2023-09-18"),
    ("zkSwap", "2023-08-22"),
    ("Connext", "2023-08-18"),
    ("Altitude (LayerZero)", "2023-08-16"),
    ("Sei #1", "2023-08-15"),
    ("Clipper", "2023-08-09"),
    ("Orchai", "2023-08-07"),
    ("Aerodrome", "2023-08-05"),
    ("CyberConnect", "2023-08-04"),
    ("SpartaDEX", "2023-07-21"),
    ("GameSwift", "2023-07-15"),
    ("Archway", "2023-07-06"),
    ("Space ID #2", "2023-06-29"),
    ("Maverick", "2023-06-28"),
    ("Pika", "2023-06-19"),
    ("Virtuswap", "2023-05-22"),
    ("zkApe", "2023-05-07"),
    ("Antimatter", "2023-04-20"),
    ("Arbitrum", "2023-03-23"),
    ("Space_ID", "2023-03-19"),
    ("Equilibre", "2023-03-01"),
    ("Zigzag", "2023-02-24"),
    ("Optimism #2", "2023-02-09"),
    ("Thena", "2023-01-15"),
    ("Hooked", "2022-12-07"),
    ("Across Protocol", "2022-11-08"),
    ("Blur Season", "2022-10-20"),
    ("Aptos", "2022-10-19"),
    ("Safe", "2022-09-01"),
    ("Stride", "2022-08-15"),
    ("Hashflow", "2022-05-10"),
    ("Hop Protocol", "2022-05-06"),
    ("Optimism", "2022-05-01"),
    ("RAW", "2022-04-19"),
    ("Galxe", "2022-03-18"),
    ("Apecoin", "2022-03-17"),
    ("Stargate Finance", "2022-03-17"),
    ("X2Y2", "2022-02-17"),
    ("CowSwap", "2022-02-11"),
    ("LooksRare", "2022-01-11"),
    ("DappRadar", "2021-12-14"),
    ("Goldfinch", "2021-12-14"),
    ("ParaSwap", "2021-11-15"),
    ("ENS", "2021-11-08"),
    ("Ampleforth", "2021-08-22"),
    ("dYdX", "2021-08-04"),
    ("Gitcoin", "2021-05-27"),
    ("Ribbon_Finance", "2021-05-25"),
    ("1inch", "2020-10-22"),
    ("Uniswap", "2020-10-12"),
    ("Aave", "2020-07-12"),
]
# Directory path to check the files
directory_path = "/home/shivam/Work/0xdroidan.github.io/_posts"

# Function to check if the file is empty
def check_and_write_file(directory_path, data):
    try:
        # Loop through each file in the directory
        for filename in os.listdir(directory_path):
            file_path = os.path.join(directory_path, filename)

            # Skip directories
            if os.path.isdir(file_path):
                continue

            # Open the file and check if it is empty
            with open(file_path, "r") as file:
                content = file.read()
                if content.strip():  # If the file is not empty
                    print(f"File {filename} already contains content.")
                    continue  # Skip this file and move to the next

            # If the file is empty, write the titles and dates
            with open(file_path, "a") as file:
                for title, date in data:
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

    except Exception as e:
        print(f"Error occurred: {e}")

# Call the function to process the directory
check_and_write_file(directory_path, data)
