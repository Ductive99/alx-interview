# UTF-8 Validation (in Python)

 In UTF-8, characters from the U+0000..U+10FFFF range (the UTF-16
   accessible range) are encoded using sequences of 1 to 4 octets.  The
   only octet of a "sequence" of one has the higher-order bit set to 0,
   the remaining 7 bits being used to encode the character number.  In a
   sequence of n octets, n>1, the initial octet has the n higher-order
   bits set to 1, followed by a bit set to 0.  The remaining bit(s) of
   that octet contain bits from the number of the character to be
   encoded.  The following octet(s) all have the higher-order bit set to
   1 and the following bit set to 0, leaving 6 bits in each to contain
   bits from the character to be encoded.
