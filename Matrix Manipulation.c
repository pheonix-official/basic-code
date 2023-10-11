#include <stdio.h>

// Function to add two matrices
void addMatrices(int firstMatrix[][100], int secondMatrix[][100], int result[][100], int rows, int columns) {
    for (int i = 0; i < rows; ++i) {
        for (int j = 0; j < columns; ++j) {
            result[i][j] = firstMatrix[i][j] + secondMatrix[i][j];
        }
    }
}

// Function to subtract two matrices
void subtractMatrices(int firstMatrix[][100], int secondMatrix[][100], int result[][100], int rows, int columns) {
    for (int i = 0; i < rows; ++i) {
        for (int j = 0; j < columns; ++j) {
            result[i][j] = firstMatrix[i][j] - secondMatrix[i][j];
        }
    }
}

// Function to display a matrix
void displayMatrix(int matrix[][100], int rows, int columns) {
    for (int i = 0; i < rows; ++i) {
        for (int j = 0; j < columns; ++j) {
            printf("%d\t", matrix[i][j]);
        }
        printf("\n");
    }
}

int main() {
    int firstMatrix[100][100], secondMatrix[100][100], resultMatrix[100][100];
    int rows, columns;

    printf("Enter the number of rows and columns for the matrices: ");
    scanf("%d %d", &rows, &columns);

    // Input for the first matrix
    printf("Enter elements of the first matrix:\n");
    for (int i = 0; i < rows; ++i) {
        for (int j = 0; j < columns; ++j) {
            scanf("%d", &firstMatrix[i][j]);
        }
    }

    // Input for the second matrix
    printf("Enter elements of the second matrix:\n");
    for (int i = 0; i < rows; ++i) {
        for (int j = 0; j < columns; ++j) {
            scanf("%d", &secondMatrix[i][j]);
        }
    }

    // Adding matrices
    addMatrices(firstMatrix, secondMatrix, resultMatrix, rows, columns);

    // Displaying the result of addition
    printf("\nSum of the matrices:\n");
    displayMatrix(resultMatrix, rows, columns);

    // Subtracting matrices
    subtractMatrices(firstMatrix, secondMatrix, resultMatrix, rows, columns);

    // Displaying the result of subtraction
    printf("\nDifference of the matrices:\n");
    displayMatrix(resultMatrix, rows, columns);

    return 0;
}
