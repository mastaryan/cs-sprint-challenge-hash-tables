def finder(files, queries):
    file_cache = {}

    result = [key for key in file_cache if len(file_cache[key]) > 0]

    return result

if __name__ == "__main__":
    files = [
        '/bin/foo',
        '/bin/bar',
        '/usr/bin/baz'
    ]
    queries = [
        "foo",
        "qux",
        "baz"
    ]
    print(finder(files, queries))