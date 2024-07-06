import os, sys, zipfile, requests
from tqdm import tqdm

default_resources = [
    "https://www.archive.org/download//romeojuliet_v4_1502_librivox/romeojuliet_v4_1502_librivox_64kb_mp3.zip",
    "https://www.archive.org/download/hamlet_1209_librivox/hamlet_1209_librivox_64kb_mp3.zip",
    "https://www.archive.org/download//as_you_like_it_version_3_2012_librivox/as_you_like_it_version_3_2012_librivox_64kb_mp3.zip",
]

def run(*resources): 
    os.makedirs("mp3/zip", exist_ok=True)
    if not len(resources): 
        resources = default_resources
    
    print(f"{os.path.basename(__file__)}: to download: {', '.join(resources)}")

    for uri in resources: 
        resource_name = uri.split('/')[-1]
        if os.path.isfile(f"mp3/zip/{resource_name}"):
            print(f"{os.path.basename(__file__)}: found resource {resource_name} => skipping download")
        else: 
            print(f"{os.path.basename(__file__)}: downloading resource {resource_name}")
            response = requests.get(uri, stream=True)
            with open(f"mp3/zip/{resource_name}", "wb") as handle:
                for data in tqdm(response.iter_content(chunk_size=1024), unit='kB'):
                    handle.write(data)

        print(f"{os.path.basename(__file__)}: extracting the archive...")
        with zipfile.ZipFile(f"mp3/zip/{resource_name}", 'r') as zip_ref:
            zip_ref.extractall("mp3")

if __name__ == "__main__": 
    os.chdir("../")
    run(*sys.argv[1:])