int foo(int a, char b, float c, char* str)
{
	return a * (int)c;
}

int main(int argc, char* argv[])
{
	return foo(1, 'a', 4.5f, "hello");
}

