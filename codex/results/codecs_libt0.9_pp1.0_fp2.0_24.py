import codecs
codecs.open("questions.txt","w",encoding="utf-8")

file_name = "questions.txt"

url = "https://www.zhihu.com/api/v4/questions/{question_id}/answers?include=data[*].is_normal,admin_closed_comment,reward_info,is_collapsed,annotation_action,annotation_detail,collapse_reason,is_sticky,collapsed_by,suggest_edit,comment_count,can_comment,content,editable_content,voteup_count,reshipment_settings,comment_permission,created_time,updated_time,review_info,relevant_info,question,excerpt,relationship.is_authorized,is_author,voting,is_thanked,is_nothelp,is_labeled,is_recognized,paid_info,paid_ info.product_id,business_status,paid_info.business_status,paid_info.paid_amount,paid_ info.refund_amount,paid_info.price,paid_info.currency,
