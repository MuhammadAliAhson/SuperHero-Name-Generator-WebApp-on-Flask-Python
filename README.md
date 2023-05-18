# Super-Hero_Name_Generator-WebApp-on-Flask(Python)
 I have trained the model for generating Super Heroes/Villans Names. I have used the Flask framework to make the WebApp to make it user friendly 

![ezgif com-video-to-gif](https://github.com/MuhammadAliAhson/Super-Hero_Name_Generator-WebApp-on-Flask-Python/assets/105967134/fc2707ec-0524-4d33-9cc7-87759aade882)


# Superhero Name Generator

This is a Python code for generating superhero names using a character-level language model. The model is trained on a dataset of superhero names and uses a tokenizer and a recurrent neural network (RNN) to generate new names based on the patterns learned from the training data.

## Prerequisites

Before running the code, make sure you have the following dependencies installed:

- numpy
- tensorflow
- matplotlib
- scikit-learn
- keras

You can install these dependencies using pip:

```
pip install numpy tensorflow matplotlib scikit-learn keras
```

## Getting Started

Follow the steps below to get started with the superhero name generator Model in Colab NoteBook:

1. Clone the repository:
   ```
   git clone https://github.com/am1tyadav/superhero
   ```

2. Open the Jupyter Notebook or Python script containing the code.

3. Run the code cells step by step. Each cell performs a specific task and outputs the results.

## Step-by-Step Guide

1. The first code cell imports the necessary libraries and prints "Done" to confirm that the libraries are imported successfully.

2. The second code cell imports additional libraries required for the model and prints "Done" to confirm the import.

3. The third code cell clones the GitHub repository that contains the superhero dataset.

4. The fourth code cell reads the data from the "superheroes.txt" file and displays the first 10 characters of the data.

5. The fifth code cell initializes a tokenizer with specific filters and split settings.

6. The sixth code cell fits the tokenizer on the data.

7. The seventh code cell creates dictionaries to map characters to indices and indices to characters.

8. The eighth code cell splits the data into individual superhero names.

9. The ninth code cell saves the tokenizer to a file named "tokenizer.pkl" using pickle.

10. The tenth code cell defines a function, `name_to_seq`, that converts a superhero name to a sequence of indices.

11. The eleventh code cell uses the `name_to_seq` function to convert the first superhero name to a sequence of indices.

12. The twelfth code cell defines a function, `seq_to_name`, that converts a sequence of indices back to a superhero name.

13. The thirteenth code cell uses the `seq_to_name` function to convert the sequence of indices back to a superhero name.

14. The fourteenth code cell creates sequences of indices from the superhero names.

15. The fifteenth code cell displays the first 10 sequences of indices.

16. The sixteenth code cell calculates the maximum length of the sequences.

17. The seventeenth code cell pads the sequences with zeros to make them all of the same length.

## Conclusion

By following the step-by-step guide, you can run the code and generate superhero names using the trained language model. The code provides functionality to preprocess the data, train the model, and generate new names based on the learned patterns. Feel free to explore and modify the code to experiment with different datasets and models. Enjoy generating superhero names!


