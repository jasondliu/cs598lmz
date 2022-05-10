import _structural_decorator.TrafficTower.TrafficTower

import scala.collection.mutable

object MainApp {
  def main(args: Array[String]): Unit = {

    // OCP
    val runtimeChecksForOCP = new RuntimeChecksForOCP
    val checkBreaks: Product => Seq[String] = (_) => {
      runtimeChecksForOCP.checkBrakes(_)
    }
    val checkEngines: Product => Seq[String] = (_) => {
      runtimeChecksForOCP.checkEngine(_)
    }
    val checkCompressors: Product => Seq[String] = (_) => {
      runtimeChecksForOCP.checkCompressors(_)
    }
    val checkLights: Product => Seq[String] = (_) => {
      runtimeChecksForOCP.checkLights(_)
    }
    val shop1 = new ProductShop(getProduct, Seq(checkBreaks, checkEngines, checkCompressors, checkLights))
    val shop2 = new ProductShop
