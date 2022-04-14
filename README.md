# Tries
A trie system that is hosted online with a global state that supports multiple concurrent clients and the following operations.

This is part of an assessment on data structures and algorithms.

## Here's the prompt:
Slingshot Data Structures and Algorithms Test 


“In computer science, a trie, also called digital tree or prefix tree, is a type of search tree, a tree data structure used for locating specific keys from within a set. These keys are most often strings, with links between nodes defined not by the entire key, but by individual characters”


Your task is to create a trie system that is hosted online with a global state that supports multiple concurrent clients and the following operations:


Add keyword to trie
Delete a keyword from trie
Search for a keyword in trie [True/False]
Return list of autocomplete suggestion based on an input prefix
Display the trie

Requirements:

The trie must be hosted online (AWS, GCloud, Azure or similar) so that multiple concurrent clients from around the world can run the aforementioned operations on the trie.
The trie must have one global state. All client operations must reflect changes in that one global state.
A client interacts with the trie through a CLI (Command-Line Interface). There should be clear instructions on how to download/install this CLI and run operations. You can make this CLI available through distributions such as `npm` (if using JS) or equivalent.
Your trie must maintain the integrity of the order of requested operations across multiple clients. If client A’s request is received before client B’s request, client A’s request must be processed first before B’s request is processed. Think about if/what data structure can help with this.
The operations must be as algorithmically efficient as you can think of.

What we’re looking for:

Good system design thinking
Good documentation
Elegantly handling errors/edge cases
Good user-CLI interface and usability
Ability to understand a complex project given limited information
Demonstration of good algorithmic and data structure fundamentals
A testing suite (we’ll especially be looking for tests that test the trie’s global state)
Creativity
Being able to learn new things on the fly without getting intimidated and being effective at Googling when stuck.

Rules:

You can search the internet for documentation, debugging.
You may search up what a trie is and how it is commonly represented, but not implementation details.
You cannot share this take-home with anybody but yourself. If you are found to be collaborating/sharing this question or your solution, you will be disqualified from our program. We use industry-grade tools such as MOSS and have easily identified malpractice in the past.
If you are found to have plagiarised code from the internet, you will also face disqualification. You can only use Google or StackOverflow code snippets to the extent that they have a non-significant overall contribution to your codebase. You must cite in comments any such code snippets used.
By attempting this challenge, you automatically agree to make your repo private after we have evaluated your submission (whether the evaluation leads to an acceptance or rejection)

Submission:

Submit a link to a GitHub repository with the following:
The server (managing the trie data structure)
The client CLI
Clear documentation on the server as a separate README.md
How the server is hosted.
How the CLI interacts with it
If you’ve made available REST endpoints for your server and how to test/use them using curl.
Clear documentation on how to install and use the CLI as a separate README.md (we will be running automation and manual tests on the CLI and server)

## Prerequisites:
- pip

## Installation
1. Download and extract the .zip file.
2. Open the main directory on a terminal.
3. Write the following in the terminal:
```sh
npm install --editable .
```
   
## Usage

  add [word] - add specified word to trie
  
  delete [word] - delete specified word to trie

  search [word] - returns whether the word is valid in the trie

  autofill [word] - returns the possible words that complete [word] in the trie

  display - displays the current state of the trie
  

## Built with
- Python
- MySQL
- AWS RDS
