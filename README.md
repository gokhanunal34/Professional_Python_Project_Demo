# What Is It?
`wordrank` is a simple tokenizer for a small use cases. It's primary purpose is to teach
students at Florida State University how to begin writing Python packages. Initial development
started in Spring 2024.

# Preface
This project has been configured for development with Visual Studio Code in a Unix-like
environment, and the instructions in this README will always default to reflect that. However,
you are free to use any editor or IDE of your choosing. Where possible, this README will
attempt to include instructions for Windows environments; where not possible/feasible,
remember that the knowledge of the world is yours for the taking on the internet.

# How Do I Get Started?
## Step 1
The first step is to acquire the project. The project consists of a root folder, within
which exist various folders and files. Those various folders hold source code packages 
and/or tests. The various files contain configuration for the project itself and the 
supporting toolchain.

If acquiring from GitHub, simply clone this repository to the desired location on your 
local system. If acquiring via archive (zip/tarball), simply unpack the archive to the 
desired location on your local system.

## Step 2
Once you have obtained/unpacked the project, you must setup the required environment file. 
To do this, simply copy the `env.sample` to a new file named `.env` in the same directory 
(the root folder of the project). This `.env` file is consumed by the `Makefile`, and is 
thus a convenient location for you to store new environment variables that may be needed 
by the project as it evolves (e.g., credentials, URLs, etc.).

## Step 3
Prepare to use the `Makefile`. This file contains various commands that greatly simplify
the management of the project and its development environment. You should take some time
and inspect the various targets defined in the `Makefile` and get familiar with them. Those
targets, all of which are marked as `.PHONY` (non-files), provide various command hooks
that can be run via `make targetName` in a terminal.

> **IMPORTANT NOTE**  
> *All `make` commands must be run from the same folder where the `Makefile` resides.   
> That is, the current working directory must be the project root when you run `make`
> commands in a terminal window.*

If you are on a Mac or *nix system, you should already have the ability to run `make` commands.
You can test for the existence of [GNU Make](https://www.gnu.org/software/make/) by running
the command `make --version`, which should return something like the following:

```bash
~/repos/wordrank (main*) » make --version
GNU Make 3.81
Copyright (C) 2006  Free Software Foundation, Inc.
This is free software; see the source for copying conditions.
There is NO warranty; not even for MERCHANTABILITY or FITNESS FOR A
PARTICULAR PURPOSE.
```

You can install `make` on Mac with Homebrew using `brew install make`. On Linux, use a 
package manager like `apt` or `pacman` to install GNU build tools; consult documentation
for your specific system (or the internet) for more detailed instructions.

If you are on a Windows system, you may need to install [GNU Make](https://www.gnu.org/software/make/).
Perhaps the easiest way to do this is via a package manager like [chocolatey](https://chocolatey.org/install).
See [this StackOverflow post](https://stackoverflow.com/questions/2532234/how-to-run-a-makefile-in-windows)
for more information.

## Step 4
Now it is time to create your local virtual environment. A virtual environment provides 
an isolated environment where a Python interpreter is installed, along with any dependencies 
needed by Python to test/execute the project.

In a terminal window, with the current working directory set to the project root, run the
command `make venv`. This will create a new virtual environment in the project root named
`.venv`. That virtual environment will contain a copy of a Python3 interpreter, and all
dependencies listed in `requirements.dev.text` and `requirements.txt` will automatically
be installed.

Every time you go to work on the project, you must activate the virtual environment. If
you are using VS Code, this should happen *automatically* due to the settings in `./.vscode/settings.json`.

> You can manually activate a virtual environment by running the command `source .venv/bin/activate`
> in a terminal window where the current working directory includes the `.venv` folder.

At the end of a development session, you can enter the command `deactivate` in a terminal
window where the current working directory includes the `.venv` folder.

You are now ready to write and test code.

# The General Development Process
> *This section is a general process only. Please see the following section for your
> specific tasking/workflow.* 

The usual workflow looks something like this:
1. Plan out what you are going to implement.
2. Write the code.
3. Test the code.
4. Repeat/profit.

The folder naming conventions are intentional and clear. Source code goes into the `src`
directory. Test code goes into the `test` folder.

## Writing Code
You have written code before, so this shouldn't be that hard. The key insight here is that
staying organized is very very important. The starter template provides a clear guide for
how to name/evolve a package.

As you write code, when you save the file it will automatically be linted and formatted
(if you are using VS Code). These actions are supported by the `Pylint` and `Black` VS Code
extensions. However, both `pylint` and `black` are specified as development requirements,
which means they are both available in the virtual environment as local commands should
you wish to run them manually, or if you are not using VS Code.

> **LINTING**  
> Linting is a process that checks your source code for syle-related errors and common
> programming bugs.  
> You can lint a single file with the command `pylint path/to/file`.

> **FORMATTING**  
> Formatting is a process that applies a consistent code format to all source code in a
> project, enhancing readability and providing the illusion that a single develolper has
> written all of the code.  
> You can format a single file with the command `black path/to/file`.

## Testing Code
Once you have written new code (or, even better *before you write any code*), it must be
tested. Tests can be added to as necessary to prove the functionality and robustness of
the project. As a professional developer, you have a responsiblity to prove that the code
you provide is fit for purpose and meets the requirements set forth by your customer.

Testing code can be done many ways with many tools. For this project, the tool of choice
is `pytest`. It is an effective unit-testing tool that is simple to use. A configuration
has already been provided in the project root via the `pytest.ini` file.

> **TESTING**  
> To run a single test module, you can use the command `pytest path/to/test/module`, or
> the command `python -m pytest path/to/test/module`.

# Your Task
Your task for this assignment is to implement the `WordRank` class template. This should
be familiar territory by now. The code you submit must have a Pylint score of *at least*
8/10 (as shown when pylint is run on wordrank.py with the command, 'pylint
./src/wordrank/wordrank.py') to receive full marks.

The `input` folder in the project root contains sample input files. You should not need
to touch these (or add any), only to know that they exist and where.

The code you submit must pass all the unit tests provided in the `testWordRank.py` module.
You can run that battery of tests using the command `make unit`.

Your code must also produce acceptable output from the `src/driver.py` file. You can run
that file using the command `make driver`. 

The expected output of `driver.py` with a correct implementation of `WordRank` is:
```bash
Creating testobj1 with exclude_stopwords = True.

Creating testobj2 with exclude_stopwords = False.

Attempting creation of testobj3 with non-utf8 file.

Unicode decode error encountered attempting to open 'non_utf8_file.txt'.

Total words read from MobyDick_Chapter1.txt: 2193.

Number of times 'ishmael' occurred in file: 2.

Count for 'and' in testobj1: 0.

Count for 'and' in testobj2: 73.

Non-stopwords that occurred 10 times in the file: ['sea', 'his', 'one'].

All words that occurred 10 times in the file: ['or', 'sea', 'his', 'one'].


Top 10 words excluding stopwords:
i 43
me 24
you 23
all 23
my 14
go 12
some 11
from 11
sea 10

Top 10 words including stopwords:
the 124
of 81
and 73
a 68
to 53
in 48
i 43
is 34
it 32
```
