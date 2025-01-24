import os

# Directory path to check the files
directory_path = "/home/shivam/Work/0xdroidan.github.io/newpros"

# Function to check if the file is empty and write the title as the file name (without .md)
def check_and_write_title(directory_path):
    try:
        # Loop through each file in the directory
        for filename in os.listdir(directory_path):
            file_path = os.path.join(directory_path, filename)

            # Skip directories and ensure the file is a markdown file
            if os.path.isdir(file_path) or not filename.endswith(".md"):
                continue

            # Open the file and check if it is empty
            with open(file_path, "r") as file:
                content = file.read()
                if content.strip():  # If the file is not empty
                    print(f"File {filename} already contains content.")
                    continue  # Skip this file and move to the next

            # If the file is empty, write the title as the file name without .md
            #title = filename.replace(".md", "")
            filename = os.path.basename(filename)
            title = filename[11:-3]
            with open(file_path, "w") as file:
               file.write(f"""---
layout: post
title: "{title}"
date: 2024-01-01
categories: []
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
check_and_write_title(directory_path)

