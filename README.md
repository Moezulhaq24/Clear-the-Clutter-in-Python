### Clear the Clutter

---

#### Overview

Clear the Clutter is a Python script designed to organize files by categorizing them into specific directories based on their file extensions. It helps users maintain a tidy file structure by automatically sorting files into predefined folders for images, documents, media files, and others.

#### Features

1. **Automatic File Organization**
   - **Categorization:** Files are categorized into different folders based on their file extensions.
   - **Supported Formats:** Recognizes and moves files of specific formats like images (.png, .jpg, .jpeg), documents (.txt, .pdf, .docs), and media files (.mp4, .mp3).
   - **Customizable:** Users can modify the script to add support for additional file formats or customize folder names.

2. **User-Friendly Operation**
   - **Ease of Use:** Simple execution by running the Python script in the directory containing the files to be organized.
   - **Efficiency:** Organizes files quickly and efficiently without manual intervention.

3. **Flexible and Scalable**
   - **Scalability:** Handles large volumes of files and adapts to different file naming conventions and extensions.
   - **Extensibility:** Easily extendable to support new file types or customize sorting criteria.

#### Usage

1. **Setup:**
   - Clone the repository or download the `main.py` script.

2. **Execution:**
   - Run the script in the directory containing the files you want to organize.
   - Files will be automatically sorted into folders named `Image`, `Docs`, `Media`, and `Others` based on their file types.

3. **Customization:**
   - Modify the `imgExtn`, `docsExtn`, `mediaExtn` lists to include additional file extensions as per your requirements.
   - Adjust folder names (`Image`, `Docs`, `Media`, `Others`) to suit your organizational preferences.

#### Implementation Details

- **Python Version:** Python 3.x
- **Dependencies:** Built-in `os` module for file operations.

#### Installation

- Clone the repository:
  ```
  git clone https://github.com/yourusername/clear-the-clutter.git
  ```
- Run the script using Python:
  ```
  python main.py
  ```

#### Contribution

Contributions to this project are welcome. You can fork the repository, make enhancements or bug fixes, and submit a pull request for review.

----------------------------------------------------------------------------------------------------------------------------------------

This readme provides an overview of the Clear the Clutter project, outlining its functionality, usage instructions, customization options, and guidelines for contribution and contact. Adapt the details based on your specific implementation before uploading it to GitHub.
 
