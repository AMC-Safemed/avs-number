#include <stdbool.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

void canonize_avs_number (char** p_str)
{
    char* str = *p_str;
    int i;
    int j;

    for (i = 0 ; str[i] != 0 ; i++) {
        if (str[i] == '.') {
            // Remove dot in place
            j = i;
            for (j = i ; str[j] != 0 ; j++) {
                str[j] = str[j+1];
            }
        }
    }
}

bool is_valid_avs_number (char* avs_no)
{
    if (strlen(avs_no) != 13) return false;

    int i;
    int total = 0;
    for (i = 0 ; i < 12 ; i += 2) {
        total += avs_no[i] - '0';
    }
    for (i = 1 ; i < 12 ; i += 2) {
        total += 3 * (avs_no[i] - '0');
    }

    int expected_key = 0;
    if (total % 10 != 0) {
        int round_ten_up = (total / 10) * 10 + 10;
        expected_key = round_ten_up - total;
    }

    int actual_key = avs_no[12] - '0';

    return actual_key == expected_key;
}



int main (int argc, char* argv[])
{
    if (argc != 2) {
        fprintf(stderr, "Usage: %s AVS_NUMBER\n", argv[0]);
        exit(EXIT_FAILURE);
    }

    char* avs_no = argv[1];
    canonize_avs_number(&avs_no);
    printf(is_valid_avs_number(avs_no) ? "Valid\n" : "Invalid\n");

    return 0;
}


