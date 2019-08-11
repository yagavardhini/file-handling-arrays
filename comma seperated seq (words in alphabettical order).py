items=input("input comma seperated words for input:")
words=[word for word in items.split(",")]
print(",".join(sorted(list(set(words)))))
