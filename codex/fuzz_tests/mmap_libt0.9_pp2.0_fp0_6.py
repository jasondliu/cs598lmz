import mmapi.ui.PlayerStatusDisplay;

	 
	public class UserMediaPlayer extends DayPlayer
	{
				
		private var mp3Player:SoundPlayer;
		private var mpegPlayer:MpegPlayer;
		private var _display:PlayerStatusDisplay;
	 
		private var _playing:Boolean = false;
		
		private var _tempo:Number = 0;
		private var _tempo_max:Number = 0;
		private var _tempo_expect:Number = 0;
		public function UserMediaPlayer()
		{
			super();
			mp3Player = new SoundPlayer ();
			mpegPlayer = new MpegPlayer ();
			mpegPlayer.showVideo = false;
			
			display = new PlayerStatusDisplay ();
		}
		
		public function set display(d:PlayerStatusDisplay):void {
			_display = d;
			this.statusRenderer = _display.getStatusRenderer();
		}


