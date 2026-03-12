CREATE TABLE IF NOT EXISTS healthcare.gold.dim_product
(
    product_key BIGINT,
    product STRING,
    product_grade STRING
)
USING DELTA;

CREATE TABLE IF NOT EXISTS healthcare.gold.dim_method
(
    method_key BIGINT,
    x_method STRING,
    stage STRING,
    units STRING
)
USING DELTA;

CREATE TABLE IF NOT EXISTS healthcare.gold.dim_status
(
    status_key BIGINT,
    status STRING,
    reportable STRING,
    x_disposed STRING
)
USING DELTA;

CREATE TABLE IF NOT EXISTS healthcare.gold.dim_batch
(
    batch_key BIGINT,
    lot_name STRING,
    lot_number INT
)
USING DELTA;

CREATE TABLE IF NOT EXISTS healthcare.gold.dim_test
(
    test_key BIGINT,
    test_number INT,
    name STRING,
    item_description STRING,
    reported_name STRING
)
USING DELTA;

CREATE TABLE IF NOT EXISTS healthcare.gold.fact_qa_tests
(
    test_id int,

    product_key BIGINT,
    method_key BIGINT,
    status_key BIGINT,
    batch_key BIGINT,
    test_key BIGINT,

    label_id STRING,
    sample_number INT,
    entry STRING,

    result_number INT,
    description STRING,

    date_completed TIMESTAMP,
    sampled_date TIMESTAMP
)
USING DELTA;