#CODE
import numpy as np
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel
from sklearn.neighbors import NearestNeighbors

# Load data from Excel file
excel_file = "dataset in excel file" 
data = pd.read_excel(excel_file)

# Drop rows with null values in 'book_desc'
data = data.dropna(subset=['book_desc'])

# Verify data loading
print("Data loaded successfully. Number of books:", data.shape[0])

# Extract features (book descriptions)
features = data["book_desc"].tolist()

# Initialize TF-IDF Vectorizer
tfidf = TfidfVectorizer(stop_words="english")

# Create TF-IDF matrix for the book descriptions
tfidf_matrix = tfidf.fit_transform(features)

# Create an index mapping for book titles
indices = pd.Series(data.index, index=data['book_title']).to_dict()

# Define function to recommend similar books
def book_recommendation(title, tfidf_matrix=tfidf_matrix, indices=indices):
    if title not in indices:
        return f"Book title '{title}' not found in the dataset."
    
    # Fit the Nearest Neighbors model
    nbrs = NearestNeighbors(n_neighbors=6, algorithm='brute', metric='cosine')
    nbrs.fit(tfidf_matrix)
    
    # Get the index of the book and find the nearest neighbors
    index = indices[title]
    distances, recommended_indices = nbrs.kneighbors(tfidf_matrix[index], n_neighbors=6)
    
    # Exclude the book itself from the recommendations
    recommended_indices = recommended_indices[0][1:]
    
    # Check if recommendations are found
    if len(recommended_indices) == 0:
        return "No recommendations found."
    
    # Return the recommended book titles
    recommended_books = data['book_title'].iloc[recommended_indices]
    return recommended_books

# Example usage
input_title = input("Enter the book name: ")
print("\nTop 5 Recommended Books:")
recommendations = book_recommendation(input_title)
print(recommendations)
