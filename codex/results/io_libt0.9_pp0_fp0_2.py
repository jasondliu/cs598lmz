import io.socket.client.Socket;

public class PlayerControl extends Fragment{


   private static PlayerControl playerControl;
   private PlayerState mPlayer;
   private TrackAdapter mTrackAdapter;
   private Playlist mPlaylist;
   private Button btnPlay, btnNext, btnPrevious, btnStop;
   private TextView mTrackTitleView, mTrackArtistView;
   private Socket mSocket;
   public PlayerControl(){
   }

   public static PlayerControl newInstance() {
      if(playerControl==null) {
         playerControl = new PlayerControl();
         playerControl.mPlayer = PlayerState.INSTANCE;
      }
      return playerControl;
   }

   @Override
   public void onCreate(Bundle savedInstanceState) {
      super.onCreate(savedInstanceState);
      mTrackAdapter = new TrackAdapter(getContext());
   }

   @Override
   public View onCreateView(LayoutInflater inflater, ViewGroup container,
                            Bundle savedInstanceState) {
      View view = inflater.inflate(R.layout.player_
