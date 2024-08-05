#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <ctype.h>

// Define the states of the NFA
typedef enum {
    START,
    IDENTIFIER,
    CONSTANT,
    OPERATOR,
    ERROR
} State;

// Define the input symbols
typedef enum {
    LETTER,
    DIGIT,
    PLUS,
    MINUS,
    TIMES,
    DIVIDE,
    EQUAL,
    NOT_EQUAL,
    LESS_THAN,
    GREATER_THAN,
    LESS_THAN_OR_EQUAL,
    GREATER_THAN_OR_EQUAL,
    ASSIGNMENT,
    LEFT_PAREN,
    RIGHT_PAREN,
    LEFT_BRACE,
    RIGHT_BRACE,
    SEMICOLON,
    OTHER
} Input;

// Function to get the next input symbol from the input string
Input getNextInput(char *input, int *index) {
    char c = input[*index];
    (*index)++;
    if (isalpha(c)) return LETTER;
    if (isdigit(c)) return DIGIT;
    if (c == '+') return PLUS;
    if (c == '-') return MINUS;
    if (c == '*') return TIMES;
    if (c == '/') return DIVIDE;
    if (c == '=') return EQUAL;
    if (c == '!') return NOT_EQUAL;
    if (c == '<') return LESS_THAN;
    if (c == '>') return GREATER_THAN;
    if (c == '(') return LEFT_PAREN;
    if (c == ')') return RIGHT_PAREN;
    if (c == '{') return LEFT_BRACE;
    if (c == '}') return RIGHT_BRACE;
    if (c == ';') return SEMICOLON;
    return OTHER;
}

// Function to run the NFA on the input string
void runNFA(char *input) {
    int index = 0;
    State state = START;
    while (index < strlen(input)) {
        Input symbol = getNextInput(input, &index);
        switch (state) {
            case START:
                if (symbol == LETTER) state = IDENTIFIER;
                else if (symbol == DIGIT) state = CONSTANT;
                else if (symbol == PLUS || symbol == MINUS || symbol == TIMES || symbol == DIVIDE ||
                         symbol == EQUAL || symbol == NOT_EQUAL || symbol == LESS_THAN || symbol == GREATER_THAN ||
                         symbol == LESS_THAN_OR_EQUAL || symbol == GREATER_THAN_OR_EQUAL || symbol == ASSIGNMENT) state = OPERATOR;
                else if (symbol == LEFT_PAREN || symbol == RIGHT_PAREN || symbol == LEFT_BRACE || symbol == RIGHT_BRACE ||
                         symbol == SEMICOLON) state = OPERATOR;
                else state = ERROR;
                break;
            case IDENTIFIER:
                if (symbol == LETTER || symbol == DIGIT) state = IDENTIFIER;
                else state = START;
                break;
            case CONSTANT:
                if (symbol == DIGIT) state = CONSTANT;
                else state = START;
                break;
            case OPERATOR:
                state = START;
                break;
            case ERROR:
                printf("Error: invalid input\n");
                return;
        }
    }
    if (state == IDENTIFIER) printf("Identifier recognized\n");
    else if (state == CONSTANT) printf("Constant recognized\n");
    else if (state == OPERATOR) printf("Operator recognized\n");
}

int main() {
    char input[100];
    printf("Enter a string: ");
    fgets(input, sizeof(input), stdin);
    input[strlen(input) - 1] = '\0'; // Remove newline character
    runNFA(input);
    return 0;
}
