from feast import Entity, FeatureView, Field, FileSource
from feast.types import Int64, String
from feast.value_type import ValueType
from datetime import timedelta

# 1. Define entity
course = Entity(
    name="co_curso",
    join_keys=["CO_CURSO"],
    value_type=ValueType.INT64
    )

# 2. Define data source
course_source = FileSource(
    path="/Users/macbookair/my_project/feature_repo/data/course_data.parquet",  # 🔧 Use relative path if possible
    timestamp_field="event_timestamp"
    # 🔍 Must exist in your data
)

# 3. Define feature view
course_fv = FeatureView(
    name="lasso_course_features",
    entities=[course],
    ttl=timedelta(days=3000),
    schema=[
        Field(name="NU_ANO_CENSO", dtype=Int64),
        Field(name="CO_CURSO", dtype=Int64),
        Field(name="NO_CURSO", dtype=String),
        Field(name="CO_IES", dtype=Int64),
        Field(name="CO_REGIAO", dtype=Int64),
        Field(name="IN_CAPITAL", dtype=Int64),
        Field(name="TP_DIMENSAO", dtype=Int64),
        Field(name="TP_ORGANIZACAO_ACADEMICA", dtype=Int64),
        Field(name="TP_CATEGORIA_ADMINISTRATIVA", dtype=Int64),
        Field(name="IN_COMUNITARIA", dtype=Int64),
        Field(name="IN_CONFESSIONAL", dtype=Int64),
        Field(name="CO_CINE_AREA_GERAL", dtype=Int64),
        Field(name="IN_GRATUITO", dtype=Int64),
        Field(name="QT_VG_TOTAL_NOTURNO", dtype=Int64),
        Field(name="QT_VG_NOVA", dtype=Int64),
        Field(name="QT_VG_PROG_ESPECIAL", dtype=Int64),
        Field(name="QT_INSCRITO_TOTAL", dtype=Int64),
        Field(name="QT_INSCRITO_TOTAL_NOTURNO", dtype=Int64),
        Field(name="QT_ING_ENEM", dtype=Int64),
        Field(name="QT_ING_VG_REMANESC", dtype=Int64),
        Field(name="QT_ING_0_17", dtype=Int64),
        Field(name="QT_ING_18_24", dtype=Int64),
        Field(name="QT_ING_25_29", dtype=Int64),
        Field(name="QT_ING_PRETA", dtype=Int64),
        Field(name="QT_ING_CORND", dtype=Int64),
        Field(name="QT_MAT_18_24", dtype=Int64),
        Field(name="QT_MAT_AMARELA", dtype=Int64),
        Field(name="QT_CONC_NOTURNO", dtype=Int64),
        Field(name="QT_CONC_18_24", dtype=Int64),
        Field(name="QT_CONC_BRANCA", dtype=Int64),
        Field(name="QT_CONC_PRETA", dtype=Int64),
        Field(name="QT_ING_FIES", dtype=Int64),
        Field(name="QT_MAT_FINANC_REEMB_OUTROS", dtype=Int64),
        Field(name="QT_MAT_PROUNII", dtype=Int64),
        Field(name="QT_MAT_PROUNIP", dtype=Int64),
        Field(name="QT_MAT_FINANC_NREEMB_OUTROS", dtype=Int64),
        Field(name="QT_CONC_FINANC_NREEMB", dtype=Int64),
        Field(name="QT_CONC_PROUNII", dtype=Int64),
        Field(name="QT_ING_RESERVA_VAGA", dtype=Int64),
        Field(name="QT_ING_RVREDEPUBLICA", dtype=Int64),
        Field(name="QT_ING_RVETNICO", dtype=Int64),
        Field(name="QT_ING_RVPDEF", dtype=Int64),
        Field(name="QT_MAT_APOIO_SOCIAL", dtype=Int64),
        Field(name="QT_CONC_APOIO_SOCIAL", dtype=Int64),
        Field(name="QT_ING_ATIV_EXTRACURRICULAR", dtype=Int64),
        Field(name="QT_CONC_ATIV_EXTRACURRICULAR", dtype=Int64)
    ],
    source=course_source,
    online=True  # 🔧 Explicitly declare that you want to serve online
)

