package {{ cookiecutter.package_name }}.jmh

import org.openjdk.jmh.annotations.*

@State(Scope.Benchmark)
@Fork(1)
@Warmup(iterations = 0)
@Measurement(iterations = 1)
open class KotlinBenchmark {
  var value: Double = 0.0

  @Setup
  fun setUp(): Unit {
    value = 3.0
  }

  @Benchmark
  fun mulBenchmark(): Double = Math.pow(value, value)

  @Benchmark
  fun mulBenchmark2(): Double = value * value
}
