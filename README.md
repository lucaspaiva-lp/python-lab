# MapReduce Word Count - Big Data

This project implements the **MapReduce** concept for processing and counting words in large volumes of text using the `mrjob` library. Developed for the Big Data course (ADS - 3rd Semester).

---

## Project Structure

* **`map-reduce.py`** : Main script containing the class that inherits from `MRJob`. It defines the **Map** (tokenization) and **Reduce** (summing occurrences) steps.
* **`raw_data.txt`** : The input file containing the raw text to be processed.
* **`qtd.txt`** : The output file generated after processing (displaying the results).

---

## Environment Setup (Virtualenv)

To avoid conflicts with the system Python on Arch Linux and permission issues with SSHFS mounts, virtual environments are stored locally in the Home directory.

### Creating the environment

**Bash**

```
# Creating a centralized directory for venvs
mkdir -p ~/.venvs

# Creating the specific environment for Big Data
python -m venv ~/.venvs/bigdata-estacio
```

### Activating the environment

**Bash**

```
source ~/.venvs/bigdata-estacio/bin/activate
```

### Installing dependencies

**Bash**

```
pip install -r requirements.txt
```

---

## How to Run

The command below reads the text file, processes the mapping and reduction steps, and redirects the output to a final file:

**Bash**

```
python map-reduce.py input_data.txt > display.txt
```

---

## Implementation Notes

* **MRJob** : Used to simplify writing MapReduce code within a single Python class, allowing for local execution or deployment on clusters (Hadoop/AWS).
* **Performance** : Processing is done via streaming, which allows handling files larger than the available RAM.
