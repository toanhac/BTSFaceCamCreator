import kagglehub

# Download latest version
path = kagglehub.dataset_download("sharad5/korean-band-bts-members-face-recognition")

print("Path to dataset files:", path)