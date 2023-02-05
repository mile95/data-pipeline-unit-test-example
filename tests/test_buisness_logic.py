from my_package.buisness_logic import append_status_column
from pyspark.sql import functions as sf


def test_append_status_column(spark_session):
    # Arrange
    sdf = spark_session.createDataFrame(
        [
            (1, "foo"),
            (2, "bar"),
        ],
        ["id", "label"],
    )

    # Act
    actual_sdf = append_status_column(sdf)

    # Assert
    assert actual_sdf.columns == ["id", "label", "status"]
    assert actual_sdf.select(sf.collect_list("status")).first()[0] == ["new", "new"]
