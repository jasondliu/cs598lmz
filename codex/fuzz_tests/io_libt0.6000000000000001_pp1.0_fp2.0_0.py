import io.realm.RealmResults;

/**
 * Created by lidu on 2017/8/7.
 */

public class HomePageAdapter extends RecyclerView.Adapter<HomePageAdapter.ViewHolder> {

    private RealmResults<DataBean> list;
    private Context mContext;

    public HomePageAdapter(Context mContext) {
        this.mContext = mContext;
    }

    public void setList(RealmResults<DataBean> list) {
        this.list = list;
        notifyDataSetChanged();
    }

    @Override
    public ViewHolder onCreateViewHolder(ViewGroup parent, int viewType) {
        return new ViewHolder(LayoutInflater.from(mContext).inflate(R.layout.item_home_page, parent, false));
    }

    @Override
    public void onBindViewHolder(ViewHolder holder, int position) {
        holder.setData(list.get(position));
    }

    @Override
    public int getItemCount() {
        return list == null ? 0 :
