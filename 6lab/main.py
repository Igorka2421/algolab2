def find_all_indices(haystack, needle):
    indices = []
    index = haystack.find(needle)
    while index != -1:
        indices.append(index)
        index = haystack.find(needle, index + 1)
    return indices

# Приклад використання:
haystack = "ababcababcabcabc"
needle = "abc"
result = find_all_indices(haystack, needle)
print("Indices of '{}' in '{}' using find_all_indices: {}".format(needle, haystack, result))
