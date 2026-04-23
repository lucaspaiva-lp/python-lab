# File Curator

A Python script designed to automate the organization of document libraries (PDF, EPUB, PPT/X). The script uses a mapping dictionary to automatically categorize files based on keywords found in their filenames.

## How it works

The script iterates through the `SOURCE_DIR`, checks if the filename contains any of the keys defined in the `mapping` dictionary, and moves the file to the corresponding destination directory.

> **Note:** The order of the keys in the `mapping` dictionary is crucial, as the script stops at the  **first match found** .

## Configuration

Before executing, verify the variables at the beginning of the script:

* **`SOURCE_DIR`** : The path containing the files to be organized.
* **`DRY_RUN`** : Set to `True` to simulate movement (results are only printed to the terminal). Set to `False` to perform the actual move operations.
* **`mapping`** : A dictionary where the key is the keyword and the value is the destination folder name.

## Usage

1. Place the script in the root of your working directory.
2. Configure `DRY_RUN = True` and execute to validate:
   **Bash**

   ```
   python organizador.py
   ```
3. After reviewing the logs, set `DRY_RUN = False` and execute again to process the organization.

## Directory Structure

The script organizes files into the following categorized structure:

* `01_arquitetura_software/`
* `02_backend_programacao/`
* `03_infra_devops/`
* `04_bancos_dados/`
* `05_frontend_mobile/`
* `06_fundamentos_hardware/`
* `07_negocios_literatura/`
