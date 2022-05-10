fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi
fn()

# This is a regression test for a bug in the bytecode interpreter.
# The bug was that the interpreter would not properly handle
# the case where the bytecode for a function contained a jump
# to a position that was greater than the length of the bytecode.
# This test case was found by fuzzing the bytecode interpreter.
def f():
    try:
        try:
            try:
                try:
                    try:
                        try:
                            try:
                                try:
                                    try:
                                        try:
                                            try:
                                                try:
                                                    try:
                                                        try:
                                                            try:
                                                                try:
                                                                    try:
                                                                        try:
                                                                            try:
                                                                                try:
                                                                                    try:
                                                                                        try:
                                                                                            try:
                                                                                                try:
                                                                                                    try:
                                                                                                        try:
                                                                                                           
