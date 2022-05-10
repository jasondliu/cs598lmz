import ctypes
# Test ctypes.CFUNCTYPE
#
#   AFIO_AFOPMODR Register (AFIO_AFOPMODR)
#    offset 0x20
#    Port Mode Register
#    The AFOPMODR register configures the pin wiring mode of each external port
#    pin (PA[15:0], PB[15:0], PC[13:0], PD[15:0] and PE[15:0] connected to an
#    AFIO mapping.
#

#
#   typedef struct {                                   /*!< AFIO_AFOPMODR Structure       */
#
#       uint32_t
#      AFOPMCSEL:3;                                       /*!< MCO PORT select               */
#      AFOP_POS_3                                            /*!< AFOPMCSEL GPO0@LSE            */                                
#      AFOP_POS_2                                            /*!< AFOPMCSEL GPO0@MCO            */
#      AFOP_POS_1                                            /*!< AFOPMCSEL UART5_RTS@MCO       */
#      AFOP_POS
