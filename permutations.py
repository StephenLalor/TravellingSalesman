def heaps_algo(seq, length):
  if length == 1:  # Base case.
    yield seq
    return
  for i in range(length):
    yield from heaps_algo(seq, length - 1)  # Length decrements on each call.
    if length & 1:  # If length is even.
      seq[0], seq[length - 1] = seq[length - 1], seq[0]  # Swap first and last.
    else:
      seq[i], seq[length - 1] = seq[length - 1], seq[i]  # Swap current and last.
