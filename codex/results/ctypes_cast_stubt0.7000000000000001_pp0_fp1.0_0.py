import ctypes
ctypes.cast(data, ctypes.POINTER(ctypes.c_void_p))

status = _lib.mqtt3_db_message_store(self.db,
                                     topic,
                                     len(topic),
                                     msg.mid,
                                     msg.qos,
                                     retained,
                                     msg.payloadlen,
                                     msg.payload,
                                     expiry_time)
</code>
mqtt3_db_message_store is declared as follows:
<code>int mqtt3_db_message_store(struct mosquitto_db *db, struct mosquitto *context, uint16_t mid, int qos, bool retain, uint32_t payloadlen, const void *payload, dbid_t store_id, uint64_t expiry_time);
</code>
I've tried the following:
<code>ctypes.cast(ctypes.c_char_p(msg.payload), ctypes.c_void_p)
</code>
and:
<code>ctypes.cast(data, ctypes.c_
