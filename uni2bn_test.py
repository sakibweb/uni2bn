import uni2bn

def test_uni2bn():
    # Test conversion from Unicode Bangla text to Bangla characters
    unicode_text = '\u0986\u09AE\u09BF \u09B8\u09BE\u0995\u09BF\u09AC\u09C7\u09B0 \u09A6\u09AC\u09BE\u09B0\u09BE \u09A4\u09C8\u09B0\u09BF\u0964'
    bangla_text = uni2bn.uni2bn(unicode_text)
    expected_result = 'আমি সাকিবের দ্বারা তৈরি।'
    # Convert both texts to Unicode for proper comparison
    assert bangla_text == expected_result, f"Expected: {expected_result.encode('unicode_escape')}, Actual: {bangla_text.encode('unicode_escape')}"

if __name__ == "__main__":
    # Run the tests when the script is executed
    import pytest
    pytest.main()
