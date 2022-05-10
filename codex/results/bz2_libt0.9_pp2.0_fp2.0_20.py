import bz2
bz2.decompress(rev$content)

# Reviews (1, 2, 4, 5, 7) are present
# Review (3) is missing
rev

# "biz_id" can be used to subset business data as well

bu_f[bu_f$business_id %in% rev$biz_id,]
</code>
<code>bu_f[bu_f$business_id %in% rev$biz_id,]</code> selects businesses that have a review.
What you can do next is a matter of your requirements.

