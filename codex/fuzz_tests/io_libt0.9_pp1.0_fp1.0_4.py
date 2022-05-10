import io.scalajs.npm.jquery._
import io.scalajs.npm.jstree._
import io.scalajs.npm.jstree.JSTree
import io.scalajs.npm.jstree.JSTree.JsTreeState
import io.scalajs.npm.jstree.JSTree.RefreshOptions
import io.scalajs.util.ScalaJsHelper._
import me.shadaj.scalapy.py
import me.shadaj.scalapy.python.Py.Buffer
import me.shadaj.scalapy.tensorflow.core.Graph
import me.shadaj.scalapy.tensorflow.core.Session

abstract class GraphView(val graph: Graph,
                         val visNetwork: VisualizationNetwork,
                         var tensorTables: Map[String, TensorTable],
                         height: Int = 300, width: Int = 300) {
  val jsTree = new JSTree(s"#${visNetwork.container}")

  def
