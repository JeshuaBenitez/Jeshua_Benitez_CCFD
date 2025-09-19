import cloudinary
import cloudinary.uploader
from pathlib import Path

# 🔑 Configura con tus credenciales
cloudinary.config( 
  cloud_name = "dbafo3bsw",
  api_key = "895187326852154",
  api_secret = "TcAjaZkC8LyDmIQOhiWGBS5zvFY"
)

# 📂 Archivos que quieres subir
datasets = [
    Path("data/creditcard_10k.csv"),
    Path("data/creditcard_5k.csv"),
    Path("data/creditcard_2_5k.csv"),
]

for dataset in datasets:
    response = cloudinary.uploader.upload(
        str(dataset),
        resource_type="raw"  # 👈 necesario para CSV
    )
    print(f"{dataset.name} -> {response['secure_url']}")
