# BookRecommendation
This project implements a book recommendation system using TF-IDF (Term Frequency-Inverse Document Frequency) and Nearest Neighbors algorithms. The system recommends books based on similar descriptions using a cosine similarity measure.

"Project Overview":

The book recommendation system analyzes a dataset of books with their respective descriptions and recommends similar books based on the description of a book that the user inputs.

"Features":

Book Title Search: Users can input a book title to receive recommendations.
TF-IDF Vectorization: Book descriptions are transformed into numerical representations using TF-IDF.
Nearest Neighbors: The system uses the Nearest Neighbors algorithm to find the most similar books.
Cosine Similarity: Similarity between books is measured using cosine distance between their TF-IDF vectors.

"Dataset":

The dataset is expected to be in an Excel file format (.xlsx) with the following columns:

book_title: The title of the book.
book_desc: The description of the book.
