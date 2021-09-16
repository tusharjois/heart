#include <stdio.h>

#define ACCESS_OK 0
#define ACCESS_ERR 1

void use()
{
	printf("ACCESS GRANTED\n");
	printf("You can now access the secret resource!\n");
}

int access()
{
	char buffer[20];

	printf("Enter some text:\n");
	scanf("%s", buffer);
	printf("You entered: %s\n", buffer);

	return ACCESS_ERR;
}

int main()
{
	if (access() != ACCESS_OK) {
		printf("ACCESS DENIED\n");
		printf("Looks like you don't know the password :(\n");
	} else {
		use();
	}

}
