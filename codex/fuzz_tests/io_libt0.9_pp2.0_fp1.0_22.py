import io.reactivex.subjects.PublishSubject;
import jp.co.tutttuwi.android.NFCReaderWriterGS.NfcUtil;
import jp.co.tutttuwi.android.NFCReaderWriterGS.R;
import jp.co.tutttuwi.android.nfcreversi.constants.Constants;
import jp.co.tutttuwi.android.nfcreversi.interfaces.IActivityUtilCallBack;
import jp.co.tutttuwi.android.nfcreversi.interfaces.ICommonUtilCallBack;
import lombok.Getter;
import lombok.Setter;
import lombok.extern.slf4j.Slf4j;

import static android.bluetooth.BluetoothProfile.STATE_CONNECTED;
import static android.content.Context.INPUT_METHOD_SERVICE;
import static android.graphics.Color.WHITE;
import static android.support.v7.appcompat.R.
