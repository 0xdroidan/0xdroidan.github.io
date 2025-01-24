import os
import re
from datetime import datetime

# Define the expanded category mapping
category_mapping = {
    # DeFi - Yield/Trading
    'Aark': ['defi', 'yield', 'aggregator'],
    'Infinex': ['defi', 'dex', 'trading'],
    'Ironclad': ['defi', 'stablecoin', 'algorithmic'],
    'Piggy-Superform': ['defi', 'synthetics', 'cross-chain'],
    'Symmio': ['defi', 'derivatives', 'synthetics'],
    'Suilend': ['defi', 'lending', 'sui'],
    'Scallop': ['defi', 'lending', 'liquidity'],
    'ZkLend': ['defi', 'lending', 'privacy'],
    'Zerolend': ['defi', 'lending', 'zero-interest'],
    'ZEX': ['defi', 'dex', 'trading'],
    'Nekodex': ['defi', 'dex', 'cross-chain'],
    'Shuffle': ['defi', 'synthetics', 'derivatives'],
    'Dragonswap-DEX': ['defi', 'dex', 'dragonchain'],
    'Filament-Finance': ['defi', 'derivatives', 'structured-products'],
    'Fyde': ['defi', 'yield', 'farming'],
    'Meteora': ['defi', 'lending', 'yield'],
    'Derive': ['defi', 'derivatives', 'development'],
    'Divvy': ['defi', 'yield', 'automation'],
    'NX-Finance': ['defi', 'products', 'traditional-finance'],
    'Ekubo': ['defi', 'trading', 'lending'],
    
    # Layer 1/2 & Infrastructure
    'Aleo': ['layer-1', 'privacy', 'blockchain'],
    'Kroma': ['layer-2', 'scaling', 'ethereum'],
    'Ionic': ['infrastructure', 'cross-chain', 'interoperability'],
    'Mystiko-Network': ['infrastructure', 'privacy', 'development'],
    'Peaq': ['infrastructure', 'iot', 'mobility'],
    'SwanChain': ['infrastructure', 'tokenization', 'real-assets'],
    'Side-Protocol': ['infrastructure', 'tokenization', 'defi'],
    'Nektar-Network': ['infrastructure', 'privacy', 'enterprise'],
    
    # Gaming/Metaverse
    'Ancient8': ['gaming', 'ecosystem', 'play-to-earn'],
    'Gaimin': ['gaming', 'computing', 'rewards'],
    'Hamster-Kombat': ['gaming', 'play-to-earn', 'mobile'],
    'Tevaera': ['gaming', 'metaverse', 'real-estate'],
    
    # Social/Identity
    'Friend-Tech': ['social', 'tokenization', 'networking'],
    'Talent-Protocol': ['social', 'professional', 'reputation'],
    'Alligned-Foundation': ['identity', 'privacy', 'security'],
    
    # Analytics/AI
    'SharpeAI': ['infrastructure', 'ai', 'analytics'],
    'Ordzaar': ['infrastructure', 'oracle', 'data'],
    
    # Specialized Platforms
    'LogX': ['infrastructure', 'logistics', 'supply-chain'],
    'Mantle-Cook': ['nft', 'culinary', 'marketplace'],
    'Purr': ['social', 'health', 'rewards'],
    'Wenwencoin': ['social', 'charity', 'environmental'],
    'River': ['infrastructure', 'streaming', 'content'],
    
    # NFT/Art
    'Cult': ['nft', 'art', 'governance']
    }

def update_markdown_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as file:
        content = file.read()

    # Extract project name from filename
    filename = os.path.basename(filepath)
    project_name = filename[11:-3]  # Remove date prefix and .md extension

    # Get categories for the project
    categories = category_mapping.get(project_name, ['uncategorized'] )
    categories_str = f"categories: {categories}"

    # Update or add categories in frontmatter
    frontmatter_pattern = r'---\n(.*?\n)---'
    frontmatter_match = re.search(frontmatter_pattern, content, re.DOTALL)

    if frontmatter_match:
        frontmatter = frontmatter_match.group(1)
        new_frontmatter = re.sub(
            r'categories:.*?\n',
            f'{categories_str}\n',
            frontmatter,
            flags=re.MULTILINE
        )
        if 'categories:' not in frontmatter:
            new_frontmatter = f'{new_frontmatter}{categories_str}\n'

        new_content = f'---\n{new_frontmatter}---\n{content[frontmatter_match.end():]}'

        with open(filepath, 'w', encoding='utf-8') as file:
            file.write(new_content)
        print(f"Updated categories for {project_name}: {categories}")
    else:
        print(f"No frontmatter found in {filepath}")

def main():
    # Get current directory
    current_dir = os.getcwd()

    # Process all markdown files with the date prefix format
    for filename in os.listdir(current_dir):
        if filename.endswith('.md') and re.match(r'\d{4}-\d{2}-\d{2}-.*\.md', filename):
            filepath = os.path.join(current_dir, filename)
            update_markdown_file(filepath)

if __name__ == "__main__":
    main()
