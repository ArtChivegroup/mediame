import os
import tkinter as tk
from tkinter import filedialog
from git import Repo
import shutil

class GitUploaderLoaderApp:
   def __init__(self, root):
       self.root = root
       self.root.title("Git Uploader dan Loader")

       self.upload_button = tk.Button(root, text="Upload Perubahan", command=self.upload_perubahan)
       self.upload_button.pack(pady=10)

       self.load_button = tk.Button(root, text="Load Repository", command=self.load_repository)
       self.load_button.pack(pady=10)

   def upload_perubahan(self):
       repo_path = filedialog.askdirectory(title="Pilih Repository Lokal")
       if repo_path and os.path.exists(os.path.join(repo_path, ".git")):
           repo = Repo(repo_path)
           status = repo.git.status()
           if 'nothing to commit' in status:
               print("Tidak ada perubahan yang perlu di-commit.")
           else:
               repo.git.add(".")
               repo.git.commit("-m", "Commit otomatis")
               repo.git.push("https://ghp_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@github.com/ArtChivegroup/mediame.git", repo.active_branch)
       else:
           print("Direktori yang dipilih bukan merupakan repository Git yang valid.")

   def load_repository(self):
       repo_path = filedialog.askdirectory(title="Pilih Folder Repository Lokal")
       if repo_path:
           if os.path.exists(repo_path) and os.path.isdir(repo_path):
               shutil.rmtree(repo_path)
           repo_url = "https://ghp_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@github.com/ArtChivegroup/mediame.git"
           Repo.clone_from(repo_url, repo_path)

if __name__ == "__main__":
   root = tk.Tk()
   app = GitUploaderLoaderApp(root)
   root.mainloop()