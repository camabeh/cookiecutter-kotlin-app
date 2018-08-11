@file:JvmName("Main")

package {{ cookiecutter.package_name }}

import kotlinx.coroutines.experimental.delay
import kotlinx.coroutines.experimental.runBlocking
import org.slf4j.LoggerFactory

object Main {
  var logger = LoggerFactory.getLogger(Main::class.java)!!

  @JvmStatic
  fun main(args: Array<String>) {
    logger.info("Hello World from Kotlin")

    {% if cookiecutter.use_coroutines  == 'y' -%}
    runBlocking {
      delay(1000)
      logger.info("Hello from Kotlin Coroutines!")
    }
    {%- endif %}
  }
}
