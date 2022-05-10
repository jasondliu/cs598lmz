import io.github.nwtgck.ticktacktoe.GameState
import io.github.nwtgck.ticktacktoe.Player

import scala.annotation.tailrec
import scala.util.{Failure, Success}
import scala.util.control.NonFatal


/**
  * IO common functions
  */
object IOFns {
  /**
    * Write a message
    * @param msg
    */
  def write(msg: String): Unit = println(msg)

  /**
    * Get a input string
    * @param askMsg  -> A message to ask
    * @param errMsg  -> Error message if it fails
    * @return
    */
  def getInputStr(askMsg: String, errMsg: String): String = {
    @tailrec
    def in(msg: String, errMsg: String): String ={
      try {
        readLine(askMsg)
      } catch {
        case NonFatal(e) =>
          write(errMsg)
          in(msg, errMsg)
      }
    }

    in
