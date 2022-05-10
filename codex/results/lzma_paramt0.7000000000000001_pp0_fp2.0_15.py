from lzma import LZMADecompressor
LZMADecompressor().decompress(preds)

plt.plot(range(3, max_depth+1), test_scores, marker='o', color='blue')
plt.fill_between(range(3, max_depth+1), test_scores - 1 * test_scores_std,\
                 test_scores + 1 * test_scores_std, alpha=0.15, color='blue')
plt.grid()
plt.xlabel('Maximum depth of the tree')
plt.ylabel('Cross-validation accuracy')
plt.tight_layout()
plt.show()

# TODO: Uncomment these lines if you wish to save the figure
# plt.savefig('figures/06_06.png', dpi=300)
# plt.savefig('figures/06_06.pdf')

print('maximum ROC AUC: {:.2f} with std: {:.2f} on max_depth = {}'.format(np.max(test_scores), \
                                                                          test_scores_std[np.
