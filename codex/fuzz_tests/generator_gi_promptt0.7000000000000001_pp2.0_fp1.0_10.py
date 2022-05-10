gi = (i for i in ())
# Test gi.gi_code.co_code
""")
        self.assertEqual(code.co_code, b"", "No opcodes generated yet")

        func()

        self.assertEqual(code.co_code, b"j\x00", "One opcode generated")


if __name__ == "__main__":
    unittest.main()
