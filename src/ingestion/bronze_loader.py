from pyspark.sql import SparkSession, DataFrame
from pyspark.sql.functions import current_timestamp
from utils.logger import get_logger


logger = get_logger("bronze_ingestion")


def load_raw_csv(
    spark: SparkSession,
    file_path: str
) -> DataFrame:
    """
    Load raw healthcare QA CSV dataset.
    """

    try:

        logger.info(f"Reading source file: {file_path}")

        df = (
            spark.read
            .format("csv")
            .option("header", True)
            .option("inferSchema", True)
            .load(file_path)
        )

        logger.info("File loaded successfully")

        return df

    except Exception as e:

        logger.error(f"Failed to read source file: {str(e)}")
        raise


def add_ingestion_metadata(df: DataFrame) -> DataFrame:
    """
    Add ingestion metadata columns.
    """

    df = df.withColumn(
        "ingestion_timestamp",
        current_timestamp()
    )

    return df


def write_bronze_table(
    spark,
    df: DataFrame,
    table_name: str
):
    """
    Drop and recreate Bronze Delta table.
    """

    try:

        logger.info(f"Dropping table if exists: {table_name}")

        spark.sql(f"DROP TABLE IF EXISTS {table_name}")

        logger.info(f"Writing data to Bronze table: {table_name}")

        (
            df.write
            .format("delta")
            .mode("overwrite")
            .saveAsTable(table_name)
        )

        logger.info("Bronze table created successfully")

    except Exception as e:

        logger.error(f"Failed writing Bronze table: {str(e)}")
        raise